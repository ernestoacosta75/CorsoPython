'''
Created on 18 lug 2018

@author: Administrator
'''

class ContactList(list):
    
    def search(self, name):
        '''Return all contacts that contain the search value
        in their name.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts        
                
class Contact:
    all_contacts = ContactList()
    
    def __init__(self, name = '', email = '', **kwargs):
        super()._init(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send "
              "{} order to {}".format(order, self.name))
        
class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key        
        return longest
    
class MailSender():
    '''Mixin class that will do the e-mailing for us.'''
    
    def send_mail(self, message):
        print("Sending mail to " + self.email)
        #Add e-mail logic here    
    
class AddressHolder(Contact, MailSender):
    def __init__(self, street = '', city = '', state = '', code = '', **kwargs):
        super()._init(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code    
    
class Friend(Contact, AddressHolder):
    '''Having two parents with __init__ methods, in the
    __init_method of this class we'll call the __init__ function
    on each of the superclasses and explicitly pass the self argument.'''
    def __init__(self, phone = '', **kwargs):
        super()._init(**kwargs)
        self.phone = phone    
                
class EmailableContact(Contact, MailSender):
    pass                


'''        
c1 = Contact("John A", "johna@example.net")        
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jena C", "jenac@example.net")

print([c.name for c in Contact.all_contacts.search('John')])

longkeys = LongNameDict()
longkeys['hello'] = 1
longkeys['longest yet'] = 5
longkeys['hello2'] = 'world'
print(longkeys.longest_key())
'''
e = EmailableContact("John Smith", "jsmith@example.net")
print(Contact.all_contacts)
print(e.send_mail("Hello, test e-mail here"))