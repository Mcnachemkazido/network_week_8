

def checking_amount_octets(octets):
    parts_octets = octets.split(".")
    if len(parts_octets) == 4:
        return True
    return False


def checking_number_octets(octets):
    parts_octets = octets.split(".")
    octets_normal = 0

    for part in parts_octets:
        if 0 <= int(part) <= 255:
            octets_normal += 1

    return octets_normal == 4


def checks_the_mask_correct(mask):
    parts_mask = mask.split(".")
    for part in parts_mask:
        part = bin(int(part))[2:]
        found_zero = False
        for m in part:
            if m == "1":
                if found_zero:
                    return False
            if m == "0":
                found_zero = True
    return True



def input_from_the_user():
    user_ip = input("input the ip number")
    user_mask = input("input dhe mask number")
    ip_right = False
    mask_right = False
    if checking_amount_octets(user_ip):
        if checking_number_octets(user_ip):
            ip_right = True
            print("good ip")
        else:
            print("Exceeds the number limits up to 255")
    else:
        print("Must be exactly 4 octets")

    if checking_amount_octets(user_mask):
        if checking_number_octets(user_mask):
            if checks_the_mask_correct(user_mask):
                mask_right = True
                print("good mask")
            else:
                print("The error must be that when converted"
                      " to binary there will be no 0 and 1 mixed in.")
        else:
            print("Exceeds the number limits up to 255")
    else:
        print("Must be exactly 4 octets")

    if ip_right and mask_right:
        return user_ip ,user_mask
    else:
        return False









