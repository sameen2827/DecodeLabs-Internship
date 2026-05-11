# ==========================================
#        GENERAL KNOWLEDGE QUIZ APP
# ==========================================

print("\n" + "=" * 50)
print("        GENERAL KNOWLEDGE QUIZ")
print("=" * 50)

# Score Variable
score = 0

# ------------------------------------------
# Question 1
# ------------------------------------------

answer1 = input("\n1. What is the capital of France? ")

# Sanitization
answer1 = answer1.strip().lower()

if answer1 == "paris":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer! Correct answer is Paris.")

# ------------------------------------------
# Question 2
# ------------------------------------------

answer2 = input("\n2. Which planet is known as the Red Planet? ")

answer2 = answer2.strip().lower()

if answer2 == "mars":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer! Correct answer is Mars.")

# ------------------------------------------
# Question 3
# ------------------------------------------

answer3 = input("\n3. Who wrote 'Harry Potter'? ")

answer3 = answer3.strip().lower()

if answer3 == "j.k. rowling" or answer3 == "jk rowling":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer! Correct answer is J.K. Rowling.")

# ------------------------------------------
# Final Score
# ------------------------------------------

print("\n" + "=" * 50)
print(f"Your Final Score is: {score}/3")
print("=" * 50)

# ------------------------------------------
# Performance Message
# ------------------------------------------

if score == 3:
    print("Excellent! Perfect Score!")
elif score == 2:
    print("Great Job!")
elif score == 1:
    print("Good Try!")
else:
    print("Better Luck Next Time!")