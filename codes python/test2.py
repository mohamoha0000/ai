import multiprocessing
import time
# دالة للعملية الأولى: تزيد المتغير المشترك
def process1(shared_value):
    for _ in range(5):
        with shared_value.get_lock():  # قفل لتجنب التداخل
            shared_value.value += 1
            print(f"العملية 1: القيمة الجديدة = {shared_value.value}")
        

# دالة للعملية الثانية: تقرأ وتعدل المتغير المشترك
def process2(shared_value):
    for _ in range(5):
        with shared_value.get_lock():  # قفل لتجنب التداخل
            print(f"العملية 2: القيمة الحالية = {shared_value.value}")
            shared_value.value += 2
     

if __name__ == "__main__":
    # إنشاء متغير مشترك (integer) بقيمة ابتدائية 0
    shared_value = multiprocessing.Value('i', 0)  # 'i' تعني integer

    # إنشاء العمليتين
    p1 = multiprocessing.Process(target=process1, args=(shared_value,))
    p2 = multiprocessing.Process(target=process2, args=(shared_value,))

    # بدء العمليتين
    p1.start()
    p2.start()

    # انتظار انتهاء العمليتين
    p1.join()
    p2.join()

    print(f"القيمة النهائية للمتغير المشترك: {shared_value.value}")