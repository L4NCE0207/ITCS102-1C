anime_list = []

while True:
    anime = input("Enter the title of an anime (or type 'exit' to finish): ")

    if anime.lower() == "exit":
        print("\nYou have exited the anime entry program.")
        break
    else:
        anime_list.append(anime)
        print(f"'{anime}' has been added to your anime list.")

print("\nYour anime list includes:")
for a in anime_list:
    print("-", a)
