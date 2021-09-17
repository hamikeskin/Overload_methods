class student:
    def __init__(self, name):
        self.name = name
    def __init__(self, name, email):
        self.name = name
        self.email = email

st = student("Greek", "God")
print(st.name)
print(st.email)