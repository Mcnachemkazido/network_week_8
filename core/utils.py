from .conversion import IPConverter

class IPv4Network:

    def __init__(self, ip_str, mask_str):
        self.ip_str = ip_str
        self.mask_str = mask_str

        self.ip_as_int = IPConverter.ip_to_int(ip_str)
        self.mask_as_int = IPConverter.ip_to_int(mask_str)

        self.network_int = 0
        self.broadcast_int = 0

    def calculate_network(self):
        self.network_int = self.ip_as_int  & self.mask_as_int


    def calculate_broadcast(self):
        network = self.network_int
        new_mask = ~self.mask_as_int & 0xFFFFFFFF
        self.broadcast_int =  network | new_mask


    def get_network_address(self):
        self.calculate_network()
        return IPConverter.int_to_ip(self.network_int)


    def get_broadcast_address(self):
        self.calculate_broadcast()
        return IPConverter.int_to_ip(self.broadcast_int)


    def check_class_type(self):
        first_octet = self.ip_as_int >> 24
        mask = 0
        class_type = 0

        if 0 <= first_octet <= 127:
            mask = 0xFF000000
            class_type = "Class A"

        elif 128 <= first_octet <= 191:
            mask = 0xFFFF0000
            class_type = "Class B"

        elif 192 <= first_octet <= 223:
            mask = 0xFFFFFF00
            class_type = "Class C"

        if mask == self.mask_as_int:
            return class_type
        else:
            return f"class lees"

    def get_total_host(self):
        network = bin(self.mask_as_int).count('1')
        host = 32 - network
        total_hosts = (2 ** host) - 2
        return total_hosts

    def get_cidr(self):
        return bin(self.mask_as_int).count("1")







