import os
import csv
''' Carlos Enrique Sánchez Martínez. 18th May 2019  IG: @Thecarlos_freeman
Final project for python course.
This Agenda can:
Add contact.
Update Contact.
Show all contacts.
Delete Contact.
Show Contact.
Exit.'''
CONTACTS = []
class Contac:
    '''def __init__(self, name, mail, phone_number):
        self.name = name
        self.mail = mail
        self.phone_number = phone_number'''
    
    def create_contact(self,new_contact):
        self.new_contac = new_contact
        same_contact = 0
        for contact in CONTACTS:
            if new_contact['name'] == contact['name']:
                same_contact += 1

        if same_contact != 0:
                print('{} is already in the contacts\' list.\n'.format(new_contact['name']))
                c = input('Press any key to continue...\n')
        else:
            CONTACTS.append(new_contact)
            print('Contact created!\n')
            c = input('Press any key to continue...\n')

        self.save()


                
        

    
    def show_contacs(self):
        print('These are your contacts: \n')
        
        for contact in CONTACTS:
            print (f'\n{contact}')
        
        c = input('Press any key to continue:\n')


    def update_contact(self,updated_contact):
        self.updated_contact = updated_contact
        
        for contact in CONTACTS:

            if contact['name'] == updated_contact['name']:

                field = updated_contact['field']
                data = updated_contact['updated_data']
                contact[field] = data
                print(f'The contact have been updated:\n{contact}')
                c = input('Press any Key to continue.\n')
                break
            else:
                print('{} is not in the contacts\' list. Verify the name of the contact.'.format(updated_contact['name']))
                c = input('Press any key to continue...\n')
                break

            self.save()
            


    def delete_contact(self,deleted_contact):
        self.deleted_contact = deleted_contact

        for contact in CONTACTS:

            if contact['name'] == deleted_contact:
                contact.clear()
                CONTACTS.remove(contact)
                c = input('Contact deleted!\nPress any key to continue.')
                break
            else:
                print('{} is not in the contacts\' list. Verify the name of the contact.'.format(deleted_contact))
                c = input('Press any key to continue...\n')
                break

        self.save()

    def save(self):
        with open ('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contact in CONTACTS:
                writer.writerow((contact['name'], contact['mail'], contact['phone_number']))
        



def run():
    contact = Contac()
    new_contact = {'name':'','mail':'', 'phone_number':''}

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            new_contact = {'name':'','mail':'', 'phone_number':''}
            new_contact ['name'] = row[0]
            new_contact ['mail'] = row[1]
            new_contact ['phone_number'] = row[2]

            contact.create_contact(new_contact)

    while True:
        os.system('clear')
        print('Welcome to your Agenda.\n')
        print('''How may I help you?\n
            [A]dd a new contact.\n
            [U]pdate an existing contact.\n
            [D]elete an existing contact.\n
            [S]how all the contacts.\n
            [E]xit.''')
        command = input('\n').lower()

        

        if command == 'a':
            os.system('clear')
            print('You\'ve selected to add a new contact.\n')
            newcontact_name = input('Please introduce the name of the new contact:\n')
            newcontact_mail = input('Please introduce the email of the new contact:\n')
            newcontact_phone_number = input('Please introduce the phone number of the new contact:\n')

            new_contact = {'name':'','mail':'', 'phone_number':''}
            new_contact ['name'] = newcontact_name
            new_contact ['mail'] = newcontact_mail
            new_contact ['phone_number'] = newcontact_phone_number
            
            contact.create_contact(new_contact)
            
            
            
        elif command == 'u':
            os.system('clear')
            print('You\'ve select update an existing contact..\n')
            updated_name = input('Please introduce the name of the contact you want to update\n')
            updated_field = input('Which data you wanna change: name | mail | phone_number \n')
            updated_data = input('Please introduce the updated data:\n')

            updated_contact = {'name':'','field':'', 'updated_data':''}
            updated_contact ['name'] = updated_name
            updated_contact ['field'] = updated_field
            updated_contact ['updated_data'] = updated_data

            contact.update_contact(updated_contact)
            


        elif command == 'd':
            os.system('clear')
            print('You\'ve selected to delete an existing contact.\n')
            deleted_contact = input('Introduce the name of the contact you wanna delete:\n')
            contact.delete_contact(deleted_contact)



        elif command == 's':
            os.system('clear')
            print('You\'ve selected to show all the contacts.\n')
            contact.show_contacs()


        elif command == 'e':
            os.system('clear')
            print('You\'ve selected to exit.\n')
            break;
        else:
            os.system('clear')
            print('That option is not availabe.\n')
            c = input('Pres any key to continue...\n')





if __name__ == '__main__':
    run()