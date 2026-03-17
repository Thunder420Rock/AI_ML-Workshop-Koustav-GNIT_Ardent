# contact Book mini project 

contact = {}

while True:
  print("\n----Contact Book-----")
  print("1.Add Contacts")
  print("2.Veiw Contacts")
  print("3.Search Contacts")
  print("4.Delete Contact")
  print("5.Exit")

  choice = input("Enter yout choice: ")

  if choice == "1":
    name = input("Enter your name: ")
    phone = input("Enter yout phone number: ")
    contact[name] = phone
    print("Contacts Added Sucessfully")
  elif choice == "2":
    if contact:
      print("\n Saved Contacts: ")
      for name, phone in contact.items():
        print(name, ":", phone)
  elif choice == "3":
    print("\n Enter contact names to search:")
    if name in contact:
      print("Phone Number: ", contact[name])
    else:
      print("Contact not found")
  elif choice == "4":
    name = input("Enter Contact name to Delete: ")
    if name in contact:
      del contact[name]
      print("Contact Deleted Sucessfully")
    else:
      print("contact not found")
if choice == "5":
  print("Existing Contact BOOK")
else:
  print("Invalid choice")
