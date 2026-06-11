favorite = {"food":"魚",
            "drink":"サイダー",
            "game":"ストリートファイター"}
my_favorite = input("キーを入れてください")

if my_favorite in favorite:
    f = favorite[my_favorite]
    print(f)
else:
    print("そのキーはありません")
