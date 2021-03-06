import ipaddress

print("Using summarize_address_range:")
ipsb = ipaddress.ip_address("172.16.0.88")
ipse = ipaddress.ip_address("172.16.0.131")
print("IP addr begin:", ipsb)
print("IP addr end:", ipse)
print("Summarized address ranges:")
print(list(ipaddress.summarize_address_range(ipsb, ipse)))

print()
print("Using collapse_addresses:")
ipnb = ipaddress.ip_network("192.3.0.0/27")
ipne = ipaddress.ip_network("192.3.0.32/28")
print("IP net begin:", ipnb)
print("IP net end:", ipne)
print("Collapsed networks:")
print(list(ipaddress.collapse_addresses([ipnb, ipne])))

print()
ipne = ipaddress.ip_network("192.3.0.32/27")
print("NEW IP net end:", ipne)
print("Collapsed networks, again:")
print(list(ipaddress.collapse_addresses([ipnb, ipne])))

print()
print("Collapsing more network objects:")
ipna = ipaddress.ip_network("192.3.0.0/27")
ipnb = ipaddress.ip_network("192.3.0.32/27")
ipnc = ipaddress.ip_network("192.3.0.64/26")
print("IP net A:", ipna)
print("IP net B:", ipnb)
print("IP net C:", ipnc)
print("Collapsed:")
print(list(ipaddress.collapse_addresses([ipna, ipnb, ipnc])))

print()
print("Partial collapse with overlapping networks:")
ipnd = ipaddress.ip_network("172.21.15.32/27")
ipne = ipaddress.ip_network("172.21.15.40/29")
ipnf = ipaddress.ip_network("172.21.15.72/29")
print("Networks:", ipnd, ipne, ipnf)
print("Collapsing attempt:")
print(list(ipaddress.collapse_addresses([ipnd, ipne, ipnf])))
