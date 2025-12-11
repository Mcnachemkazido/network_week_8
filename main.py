from core.user_input import input_from_the_user
from core.utils import IPv4Network
from core import output_string

incorrectly_pressed = True
while incorrectly_pressed:
    user_input = input_from_the_user()
    if user_input:
        incorrectly_pressed = False
        ip = IPv4Network(user_input[0],user_input[1])
        ip_str = output_string.format_input_ip(ip.ip_str)
        mask_str = output_string.format_subnet_mask(ip.mask_str)
        type_class = output_string.format_classful_status(ip.check_class_type())
        network= output_string.format_network_address(ip.get_network_address())
        broadcast = output_string.format_broadcast_address(ip.get_broadcast_address())
        total_host = output_string.format_num_hosts(ip.get_total_host())
        cidr = output_string.format_cidr_mask(ip.get_cidr())
        total = f"{ip_str}\n{mask_str}\n{type_class}\n{mask_str}\n{network}\n{broadcast}\n{total_host}\n{cidr}"
        with open("subnet_info_[10.50.200.7]_[212317317].txt","w") as file:
            file.write(total)
            print("Successfully written to file")
