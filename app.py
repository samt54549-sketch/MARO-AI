# MARO AI Assistant
print("أهلاً بك! أنا المساعد الذكي MARO.")

while True:
    user_question = input("اسألني شيئاً (اكتب 'خروج' للإنهاء): ")
    if user_question == "خروج":
        print("مع السلامة! نتمنى لك يوماً سعيداً.")
        break
    elif user_question.strip() != "":
        print(f"MARO يرد عليك: لقد تلقيت سؤالك '{user_question}' وأنا أعمل على تحليله للإجابة عليك بدقة!")
