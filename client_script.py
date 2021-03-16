from class1 import Account
chiara_account = Account("Chiara", "Dinan", 23, 150)

print(f"Welcome to our bank, {chiara_account._name}! Your onetime passcode is: {chiara_account.generate_onetime_passcode}. "
      f"Please "
      f"keep "
      f"it "
      f"somewhere safe.")

print(chiara_account.user_input())

