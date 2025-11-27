# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inowak-- <inowak--@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/28 17:21:59 by inowak--          #+#    #+#              #
#    Updated: 2025/11/27 17:32:20 by inowak--         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:

    objecttype = type(object)

    if (objecttype == list):
        print("List :", objecttype)
    elif (objecttype == tuple):
        print("Tuple :", objecttype)
    elif (objecttype == set):
        print("Set :", objecttype)
    elif (objecttype == dict):
        print("Dict :", objecttype)
    elif (objecttype == str):
        print(object, "is in the kitchen :", objecttype)
    else:
        print("Type not found")
    return 42