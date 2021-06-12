films ={
    "dabang":[18,5],
    "chanaiexpress":[18,6],
    "doraemon":[3,5],
    "tarzan":[15,8]
}
while True:
    choice=input("what film do you lik to watch?:").strip()
    if choice in films:
        age=int(input("How old are you?:").strip())

        if age >= films[choice][0]:
            
            num_seats=films[choice][1]

            if num_seats >0:
                print("seats are avilable")
                films[choice][1]=films[choice][1]-1
            else:
                print("no tickets")
                
        else:
            print("you are too ynoung to wathch this film")
    else :
        print("we don't hve this film")
    
