todo_list = []

def show_menu():
    print("\n1. Görev Ekle\n2. Görevleri Göster\n3. Görev Sil\n4. Çıkış")

while True:
    show_menu()
    secim = input("Seçiminiz: ")

    if secim == "1":
        görev = input("Yeni görev girin: ")
        todo_list.append(görev)
    elif secim == "2":
        for i, görev in enumerate(todo_list):
            print(f"{i+1}. {görev}")
    elif secim == "3":
        sil = int(input("Silinecek görev numarası: "))
        if 0 < sil <= len(todo_list):
            del todo_list[sil-1]
    elif secim == "4":
        break
    else:
        print("Geçersiz seçim.")
