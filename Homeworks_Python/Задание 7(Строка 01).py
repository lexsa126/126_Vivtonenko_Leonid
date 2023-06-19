def search_substr(subst, st):
    if subst.lower() in st.lower():
        return "Есть контакт!"
    else:
        return "Мимо!"
variant = search_substr("Илон Маск", "Илон Маск - инженер")
print(variant)
