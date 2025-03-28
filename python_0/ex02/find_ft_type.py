# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inowak-- <inowak--@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/28 17:21:59 by inowak--          #+#    #+#              #
#    Updated: 2025/03/28 17:40:17 by inowak--         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:

    objecttype = type(object)

    if (objecttype == list):
        print("List : <class 'list'>")
    elif (objecttype == tuple):
        print("Tuple : <class 'tuple'>")
    elif (objecttype == set):
        print("Set : <class 'set'>")
    elif (objecttype == dict):
        print("Dict : <class 'dict'>")
    elif (objecttype == str):
        print(object, "is in the kitchen : <class 'str'>")
    else:
        print("Type not found")
    return 42