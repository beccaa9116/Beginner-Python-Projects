#let us make a currency converter in python

#title
print("\nCurrency conventer\n\n 1. EUR \n 2. USD \n 3. GBP \n 4. DKK \n 5. CAD \n")


money=0
while True:
 
 #getting the inital currency and amount to convert
 choice1 = input("\nWhat is your initial currency? (1, 2, 3, 4, 5): \n")
 if choice1 in ('1','2','3','4', '5'):
  try:
   money = float(input("\nYour desired amount to convert is: \n"))
  except ValueError:
   print("Wrong input. Please try again.")
   continue
 
 #now I will just define relations between the currencies, to keep it out of the actual code as there are quite a few
 # I am not using any realtime stuff or anything because I really just want to practice basic code, operations, loops and stuff (so very basic, but still fun)

  eur_usd = float(money*(1.06))
  eur_gbp = float(money*(0.88))
  eur_dkk = float(money*(7.44))
  eur_cad = float(money*(1.43))

  usd_eur = float(money*(0.95))
  usd_gbp = float(money*(0.83))
  usd_dkk = float(money*(7.05))
  usd_cad = float(money*(1.36))

  gbp_eur = float(money*(1.14))
  gbp_usd = float(money*(1.20))
  gbp_dkk = float(money*(8.45))
  gbp_cad = float(money*(1.63))

  dkk_eur = float(money*(0.13))
  dkk_usd = float(money*(0.14))
  dkk_gbp = float(money*(0.12))
  dkk_cad = float(money*(0.19))

  cad_eur = float(money*(0.70))
  cad_usd = float(money*(0.74))
  cad_gbp = float(money*(0.61))
  cad_dkk = float(money*(5.19))

  choice2 = input("\nTo which currency you want to convert? (1, 2, 3, 4, 5): \n")
  if choice2 in ('1', '2', '3', '4', '5'):

   if choice1 == choice2:
    print(f"\nYou chose the same currency, your amount stays the same: {money}")

   elif choice1 == '1' and choice2 == '2':
    print(f"\n\n\nYour amount converted from EUR to USD is: {eur_usd}")

   elif choice1 == '1' and choice2 == '3':
    print(f"\n\n\nYour amount converted from EUR to GBP is: {eur_gbp}")

   elif choice1 == '1' and choice2 == '4':
    print(f"\n\n\nYour amount converted from EUR to DKK is: {eur_dkk}")

   elif choice1 == '1' and choice2 == '5':
    print(f"\n\n\nYour amount converted from EUR to CAD is: {eur_cad}")

   elif choice1 == '2' and choice2 == '1':
    print(f"\n\n\nYour amount converted from USD to EUD is: {usd_eur}")

   elif choice1 == '2' and choice2 == '3':
    print(f"\n\n\nYour amount converted from USD to GBP is: {usd_gbp}")

   elif choice1 == '2' and choice2 == '4':
    print(f"\n\n\nYour amount converted from USD to DKK is: {usd_dkk}")

   elif choice1 == '2' and choice2 == '5':
    print(f"\n\n\nYour amount converted from USD to CAD is: {usd_cad}")

   elif choice1 == '3' and choice2 == '1':
    print(f"\n\n\nYour amount converted from GBP to EUR is: {gbp_eur}")

   elif choice1 == '3' and choice2 == '2':
    print(f"\n\n\nYour amount converted from GBP to USD is: {gbp_usd}")

   elif choice1 == '3' and choice2 == '4':
    print(f"\n\n\nYour amount converted from GBP to DKK is: {gbp_dkk}")

   elif choice1 == '3' and choice2 == '5':
    print(f"\n\n\nYour amount converted from GBP to CAD is: {gbp_cad}")

   elif choice1 == '4' and choice2 == '1':
    print(f"\n\n\nYour amount converted from DKK to EUR is: {dkk_eur}")

   elif choice1 == '4' and choice2 == '2':
    print(f"\n\n\nYour amount converted from DKK to USD is: {dkk_usd}")

   elif choice1 == '4' and choice2 == '3':
    print(f"\n\n\nYour amount converted from DKK to GBP is: {dkk_gbp}")

   elif choice1 == '4' and choice2 == '5':
    print(f"\n\n\nYour amount converted from DKK to CAD is: {dkk_cad}")

   elif choice1 == '5' and choice2 == '1':
    print(f"\n\n\nYour amount converted from CAD to EUR is: {cad_eur}")

   elif choice1 == '5' and choice2 == '2':
    print(f"\n\n\nYour amount converted from CAD to USD is: {cad_usd}")

   elif choice1 == '5' and choice2 == '3':
    print(f"\n\n\nYour amount converted from CAD to GBP is: {cad_gbp}")

   elif choice1 == '5' and choice2 == '4':
    print(f"\n\n\nYour amount converted from CAD to DKK is: {cad_dkk}")
  else:
   print("\nWe do not have such currency. Please try again.")
 else:
   print("\nWe do not have such currency. Please try again.")

 next_one = input("\n\n\nWant to do more calculations?: (yes/no): ")
 if next_one == "no":
    break


