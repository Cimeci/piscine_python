# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: inowak-- <inowak--@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/28 11:37:15 by inowak--          #+#    #+#              #
#    Updated: 2025/03/28 16:28:10 by inowak--         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$

import time

timeout = time.clock_gettime(0)
actualtime = time.strftime("%b %d %Y")

print("Seconds since January 1, 1970:", "{:,.4f}".format(timeout), "or", "{:,.2e}".format(timeout), "in scientific notation")
print(actualtime)