from app.client.client import Client


client = Client()


ifaces = client.network.get_ifaces()
print(ifaces)


# set hostname
hn = client.network.get_hostname()
print(hn)
client.network.set_hostname('my-hostname')
hn = client.network.get_hostname()
print(hn)
