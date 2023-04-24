import paramiko
from classes import *       # class aveliable: "RouterConnection", 
from functools import *     # function avelable: "execute_command", "close", 


# Create a new router connection object
router = RouterConnection('hostname', 'username', 'password')

# Execute a command on the router
output = router.execute_command('show interfaces')

# Print the output
print(output)

# Close the router connection
router.close()

