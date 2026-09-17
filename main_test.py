from database import create_connection
from customer_repository import CustomerRepository
from interaction_repository import InteractionRepository
from follow_up_repository import FollowUpRepository

connection = create_connection()


customer_repo = CustomerRepository(connection)
interaction_repo = InteractionRepository(connection)
follow_up_repo = FollowUpRepository(connection)

#------------------------------------
#customer

customer_repo.add("alireza amiri","09194218908","a.amiri@gmail.com","A","manager","2026","first customer")
customer_repo.add("amir akbari","09195282073","amirakbari@gmail.com","B","salary manager","2026","second customer")

#-------------------------------------
#interaction

interaction_repo.add_interaction(1,"call","2026","first contact","talk about price","will follow")
interaction_repo.add_interaction(1,"meeting","2026","person meeting","rewiewed","requested changed")
interaction_repo.add_interaction(1,"email","2026","follow up email","sent subject","wating for response")
interaction_repo.add_interaction(2,"call","2026","introduction call","new load","meeting")


#-----------------------------------
#follow ups

follow_up_repo.add_follow_up(1,"2026","call about work","cheeck that")

follow_up_repo.add_follow_up(1,"2026","send final contract","description")


print(interaction_repo.get_by_customer_id(1))
print(follow_up_repo.get_by_customer_id(1))



#--------------------------
#update interaction

interaction_repo.update_interaction(1,"meeting","2026","update subject","update notes","update result")
print(interaction_repo.get_by_customer_id(1))



#------------------------
#delete interaction

interaction_repo.delete(2)
print(interaction_repo.get_by_customer_id(1))


#----------------
#switch folloW up

follow_up_repo.switch_status(1,"undone")
print(follow_up_repo.get_by_customer_id(1))

