#1. example.pyを作成して「hello world」と出力してください。
print("hello world")

#2. greet関数を実装し、「こんにちは」と出力するようにしてください。関数を呼び出して、実際に出力されることを確認してください。
def greet():
    print("こんにちは")

greet()

#3. nameを引数に取り、「私の名前は{name}です」と出力するprint_name関数を実装し、関数を呼び出して動作を確認してください。
def print_name(name):
    print(f"私の名前は{name}です")

print_name("ゆきんこ")

#4. 「おはようございます」という文字列を戻り値として返すget_greet関数を実装し、戻り値をprint関数で出力してください。
def get_greet():
    string = "おはようございます"
    return string

print(get_greet()) 
    
#5. a, bを引数に取り、その足し算の結果を戻り値として返すadd関数を実装し、関数を呼び出して結果をprint関数で出力してください。
def add(a, b):
    return a + b 

print(add(8, 7))

#6. example.pyをリポジトリにコミットし、pushしてください。
#git remote add origin git@github.com:yuukyy1125/python_Test_App.git
#git push -u origin main

#上記のコードを実際に実行した動画をloomで撮影し、GithubのREADMEに添付してください。
#スクリプトの実行はGUIからではなくターミナルからコマンドを入力して実行してください。
#リンク：https://www.loom.com/share/878f26f3956f450081d37c2084e1b386?sid=d380ffe2-13e3-4f7a-b80e-26c8a5e5023c

#Pythonの課題のGithubリンク
#リンク：https://github.com/yuukyy1125/python_Test_App.git