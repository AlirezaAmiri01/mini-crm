from database import create_connection
from customer_repository import CustomerRepository
from interaction_repository import InteractionRepository
from follow_up_repository import FollowUpRepository
from customer_db_validators import validate_phone_not_dupliacte
from dashboard_repository import count_today_follow_ups,count_open_follow_ups,count_interactions,count_customers

connection = create_connection()


customer_repo = CustomerRepository(connection)
interaction_repo = InteractionRepository(connection)
follow_up_repo = FollowUpRepository(connection)

#------------------------------------
#customer

customer_repo.add("alireza amiri","09194218908","a.amiri@gmail.com","A","manager","2026-10-11","first customer")
customer_repo.add("amir akbari","09195282073","amirakbari@gmail.com","B","salary manager","2026-10-11","second customer")

#-------------------------------------
#interaction

interaction_repo.add_interaction(1,"call","2026-10-11","first contact","talk about price","will follow")
interaction_repo.add_interaction(1,"meeting","2026-10-11","person meeting","rewiewed","requested changed")
interaction_repo.add_interaction(1,"email","2026-10-11","follow up email","sent subject","wating for response")
interaction_repo.add_interaction(2,"call","2026-10-11","introduction call","new load","meeting")


#-----------------------------------
#follow ups

follow_up_repo.add_follow_up(1,"2026-10-11","call about work","cheeck that")

follow_up_repo.add_follow_up(1,"2026-10-11","send final contract","description")


print(interaction_repo.get_by_customer_id(1))
print(follow_up_repo.get_by_customer_id(1))



#--------------------------
#update interaction

interaction_repo.update_interaction(1,"meeting","2026-10-11","update subject","update notes","update result")
print(interaction_repo.get_by_customer_id(1))



#------------------------
#delete interaction

interaction_repo.delete(2)
print(interaction_repo.get_by_customer_id(1))


#----------------
#switch folloW up

follow_up_repo.switch_status(1,"undone")
print(follow_up_repo.get_by_customer_id(1))



customer_repo.delete(1)
print(customer_repo.get_all())

print(customer_repo.get_by_id(1))


result = customer_repo.add("","09194218908","a.amiri@gmail.com","A","manager","2026-10-11","first customer")
print(result)


result = validate_phone_not_dupliacte("09194218908",connection,0)
print(result)


result = customer_repo.add("alireza","09194218908","@email","company","ceo","10-112026","notes")
print(result)

result = customer_repo.update(2,"amir akbari","09194218908","amirakbari@gmail.com","B","salary manager","second customer")
print(result)

result = customer_repo.update(2,"amir akbari","09195282073","amirakbari@gmail.com","B","salary manager","second customer")
print(result)


# ============================================
# validators test
# ============================================

print("--- Customer validations ---")

# empty name
result = customer_repo.add("", "09120000001", "a@test.com", "A", "manager", "2026-11-10", "notes")
print("empty name:", result)

# empty phone
result = customer_repo.add("test name", "", "a@test.com", "A", "manager", "2026-11-10", "notes")
print("empty phone:", result)

# word phone
result = customer_repo.add("test name", "phone", "a@test.com", "A", "manager", "2026-11-10", "notes")
print("phone as word:", result)

# wrong format phone
result = customer_repo.add("test name", "123456", "a@test.com", "A", "manager", "2026-11-10", "notes")
print("wrong phone format:", result)

# wrong date
result = customer_repo.add("test name", "09120000002", "a@test.com", "A", "manager", "10-11-2026", "notes")
print("wrong registered_at format:", result)

# wrong email foramt
result = customer_repo.add("test name", "09120000003", "a-test.com", "A", "manager", "2026-11-10", "notes")
print("wrong email format:", result)

#true
result = customer_repo.add("test name", "09120000004", "a@test.com", "A", "manager", "2026-11-10", "notes")
print("valid customer (should be None):", result)

# duplicate phone
result = customer_repo.add("another name", "09120000004", "b@test.com", "B", "staff", "2026-11-10", "notes")
print("duplicate phone:", result)


print("\n--- Interaction validations ---")

#type not in list
result = interaction_repo.add_interaction(1, "whatsapp", "2026-11-10", "subject", "notes", "result")
print("wrong type:", result)

# wrong format date
result = interaction_repo.add_interaction(1, "call", "10-11-2026", "subject", "notes", "result")
print("wrong date format:", result)

# empty subject
result = interaction_repo.add_interaction(1, "call", "2026-11-10", "", "notes", "result")
print("empty subject:", result)

# true
result = interaction_repo.add_interaction(1, "call", "2026-11-10", "subject", "notes", "result")
print("valid interaction (should be None):", result)


print("\n--- FollowUp validations ---")

# wrong format date
result = follow_up_repo.add_follow_up(1, "2026", "subject", "description")
print("wrong date format:", result)

# subject  empty
result = follow_up_repo.add_follow_up(1, "2026-11-10", "", "description")
print("empty subject:", result)

# true
result = follow_up_repo.add_follow_up(1, "2026-11-10", "subject", "description")
print("valid follow_up (should be None):", result)



print("--- Search tests ---")

# search with part of name
print("search 'ali':", customer_repo.search("ali"))

#search with part of phone 
print("search '0912':", customer_repo.search("0912"))

# search for somthing dont exitsts
print("search 'nobody':", customer_repo.search("nobody"))

#search every thing
print("search '':", customer_repo.search(""))

print("total cutomers:",count_customers(connection))
print ("open follow-ups:",count_open_follow_ups(connection))
print("todays follow-ups",count_today_follow_ups(connection))
print("total interactions: ",count_interactions(connection))
