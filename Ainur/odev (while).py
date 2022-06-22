
text = """
   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam id quam tincidunt, sollicitudin diam vel, dignissim enim. Integer id porta velit. Fusce et posuere lectus, a consequat nisl. Donec ut ex posuere, gravida ligula sit amet, rhoncus risus. Cras dapibus ipsum at nisl laoreet, ac efficitur nibh bibendum. In enim neque, dictum ac justo rhoncus, consequat faucibus urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nullam varius eu felis eu finibus. Sed venenatis iaculis mauris nec porta. Nullam rutrum odio egestas ligula tempor venenatis. Sed efficitur, justo vel viverra varius, lacus enim sagittis dui, id posuere lorem odio nec nisl. Ut urna lacus, convallis lobortis convallis ut, venenatis sit amet leo. Mauris facilisis vitae tellus sit amet sollicitudin .
   """
 
List = text.split()
z = []
for i in List:
    if (len(i)) > 9: 
        z.append(str(i))
        #print(z)
new_word = z
new_list = []
new_list.append(str(new_word))

print('New list :', new_list)
