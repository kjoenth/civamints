#!/usr/bin/python

# This shitshow is matt's fault, so it's all copyrighted and stuff by him:
# copyright 2012: matthew j weaver
# you can do whatever the fuck you please with this file as long as you keep
# this notice intact:
#
#   #####    ###   #     #    #    #     #   ###   #     # #######  #####
#  #     #    #    #     #   # #   ##   ##    #    ##    #    #    #     #
#  #          #    #     #  #   #  # # # #    #    # #   #    #    #
#  #          #    #     # #     # #  #  #    #    #  #  #    #     #####
#  #          #     #   #  ####### #     #    #    #   # #    #          #
#  #     #    #      # #   #     # #     #    #    #    ##    #    #     #
#   #####    ###      #    #     # #     #   ###   #     #    #     #####


import os
import os.path
import re
import sys

#k_civamints_dir = "/Users/matt/Dropbox/Civ PBEM/IB 20120222"
#==if you want to just run the script from in the dropbox, use the following (STH 12.06.01)===
k_civamints_dir = os.getcwd()+"/IB 20120222"
k_savegame_pattern = "IB_20120222_[^.]*[.]CivBeyondSwordSave"
k_savegame_re = re.compile(k_savegame_pattern)
k_stupid_human = """
  Look, I'm not the smart one in the room.
  That's your job. Get it together.
"""
k_sucka_mcs = [ "Giles", "JWM", "MJW", "Rory", "seant" ]
k_valid_mc_pairs = (("Rory", "MJW"), ("MJW", "JWM"), ("JWM", "Giles"),
                    ("Giles", "seant"), ("seant", "Rory"))
insertHtml=""
shamefulHtml="""<html><title>CIVAMINTS</title><body><center><h1>Civamints</h1></center><center><!--deep fucking magic. STH 12.06.01--><img border=1 src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBhQSEBUUExQVFRQVFhQXFxcYFRcVFhUYFRcVFBUUFBcXHCYeFxwkGhcYHy8gJCcpLCwsFR4xNTAqNSYrLCkBCQoKDgwOGg8PGikfHBwpKSwpKSwpKSwpKSwsKSkpKSksKSksKSwsKSkpKSwpKSksKSwpLCkpLCwsKSwsKSwsLP/AABEIAMIBAwMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAAFAAECAwQGBwj/xAA+EAABAwIEAwYFAgUDAwUBAAABAAIRAyEEEjFBBVFhBiJxgZGxEzKhwfAHQhQj0eHxcoKyFVJiU3OSosJD/8QAGAEAAwEBAAAAAAAAAAAAAAAAAAECAwT/xAAeEQEBAQEAAwADAQAAAAAAAAAAARECEiExA0FRE//aAAwDAQACEQMRAD8A8ZawErU2jLZmFloCSFsPdInRZt4xvnRaaLSbEwrcVSGUEWUcKzlqgYmcJHeWGp8xuiTqZiJWfE0xaAgWK8HVh19wiTjDbaoI5hlaqLzFlUuCN9Z8i6voUWtGbWyobUBb1U2UzCvDVV6pi2spMxJyxzT1G6yLKFNhJBiyn2CbSja6v+DPSVdRvYXlepdiv0jzBtfGgj/to6HoahnQ/wDahNsjzvgPZDFY54bQplzQYLz3abfFx9hJXqfD/wBD2Bo+NiXExcMYAJi8F079F6LhqDKTAym1rGNsA0AAeACtD1UZXuuOpfpBw4fMx7zb5qh6HRsfhVPE/wBJMG5kUg+kYiQS7cXgnXbz8F27is1R1/z8CafKvnPth2ErYKocwmkT3KgFj0dyOnqueosgQV9QcRwrK1N1N7Q5jgQQRMzb8K+f+2HZR2BxJYMzqb703HUjdp6hFmNOet+glSmeeyq8U1cmJM2UGVydiUtWvrt7izAczARDEYc5Jy6ob8M6H0KXQJ2sAqTz4eKlTaBraE7m6Qpw0X1IGl1lm/JarG+6pdMylQdjU1VsDVXUBOmqrrTpH0SsNGmZU3ug+KqoYedSt3wg2EQMb9fmSVlRlzokmA+i7vIlVcABuhrmRdam1ZU0o002AwSk8gX0VRaXCApU8PeH6Jwz0zIJ16qRbLSpMpABWBk2nZGAJLTqrsA7vRqE9VureqngaUO1RCxc+lHqpfxrj3VLENLj4LG5pDlVuG3vqiNbqAmBCz5F03YHs47HYtlE92mO/UPJjYkDqbAeM7J6Vrt/0f7CZiMbV+RpIpNIBzuFjUMjQGwi8jpf2ByVKi1jA1rQ1jQAGgQABYABVvqKo57baRKXxFnNQlN8RRejkafiqqq0H8lV/FUw4c5KrmlYpqOj+v8Ahc52y4MMVhy0/O3vMPJw2HiLea6SsyQheJtqtBHz7XwUHv6yZG6pwtZrXENHqun/AFA4YKWJL26VBmA5HRw9b+a42mcr5Kz6dEuir8XIWXEOaXA6RvHunNQXKogkQYn7Kao9fCSMzbzssdN20EEIm2plb1VZoioMw7r/AHSlTjA48gq6hiFoe297HeyrqUiQE6EaLuWqnUcYvqmwrbrW+lodfzdEhqcOzKJ9Vdi3HMPBP8SJtroncJgn0TkNmewykrH12A6pJEGPaFGlUieSqdUTtepxOiWErN0VrngoSwJMxGWY3QejLWzpor2CDJQejxVzRAVv/WJKcLYtxcTexWag4BwT4rEtcZlZviCdUX6ej4ptdoUzwwGzVgweMaDcq1/EG7FXs+jV7KMu012C99/Tnsf/AAOHDniK9YAv5sbq2n9z18Fx36NdjfjvGMqj+VTP8sEfPUH7uob7+C9fxDu/PJK/GfV30scqHx4LQ1trqp7Z/PdTqWZxUGmQnrAaKDXWWVvtc+HJgc0zqpH+VFzlRUy7rTlNWurc1mxN0gGkXJJ8Y9FHTw9lvEVwX6hcNz0c29MyPB1iPWCvK8TTDb7r3Dtnhc2ErdKbyNvlGcey+eq+OLjKXa+OvQ2wzpCZ2GvN0Hp8Ve3SPRRfxSof3KMjTzg02oDY6hWPAtBAK5p1dxMyVEuPMpYXmNYnFgvi0DU81T/G09ZNhohKScLyF6XE6Y2Mqqpxt37QAhqdGl5VpqcSe7U/RUOrE7lQSQW08pJkkEZJSypiEA0pJ0ggGTwpgKYpparxUwnyrU2kFEC6Wn4qAxG+yfZp+NxdKgyxe4STo1ou5x5wFnoYaQvev0R7JNo4c4tw/mVpa2R8tMHbxI+gR7osx6Jw3htPD0GUaTQ1lNoa0AQIH5PmstQy88giVXRYPh9884CKiNFazRzWd4gbrbM6RAVDn7apUQPeOarFMlX4gAGVS+pAWPTSMWLfGqytdm3IHj+XT4506rAXCwEzfRPi+zsbzUaLSPr91KxibrGKjfE/X1Uw6dD5ErqlY2H4pTmmWm4IIM7g29F8xYillc4ciRz0ML6erk5DzXzt2twPwsbXbEAVHEeBMghPv4OQWEylCULNWIp1INSAQMRTKUKKASdJMmRJ0ydANKSSSAcuUSUUqcBeNFmfwx42RisrM1qmaakKDgdFN6m1UiDWq1oTUwrxSKSleaynQwpdoCSTAA1PQLpOyXYivxCqGUmw0Hv1CO4wdeZ5AL33sl2DwvDmdxuerHeqvAzHnlH7B0CfinrrHlXY79IMXWLXV2/ApEgnOYqFu+VlyDH/AHR5r37CYVtNjWMENY0NaOQAgBZamNG2q10KwcJCN/SLbUnBD6sgyN/ZECsdZsg/nRKlDYd3dMrN/wBVpyWA3H1TUq80yNwVyFWi5mIfMxqOoRsPHU1jOiwuc+en5oq8FjJgf5RCo8Bp3Kws320lwLr0iRCxDDuEwEROMHRI1AR+XV8SUqyUsIT/AJj6LXT4GQ0vfUDfMn3Q6pxIUz4D2v7IXxztP8RopsOtj4n+3stebtxF+CtRpBIsQdxuuD7Z/pXia9V2JofDc19y0Eh2lyWkRNtjflOvcYf5QNgB7Ixg8YWgD7/Zb2SzGe4+WMThSx5a4FrmkggiCCNiDoqnNXs/6w9k21Kf8XSADmWqAN+YE/MY3C8Zc1Y9TLjbm7D0xqoBqupahNXbBKlWKFFSUSFTMkkkkAkydJAMknSQQ1i8c+YzDyWd9STLifVDsyWdF2tfJufihEN9VBtRsXF+ax5kpQXk0NrCeiL8IwD8RVZSpNzPe4NaOZPsgIK93/QjsoGUnY2o3vOllKR8rRZzhI30kbApZ7Lyegdk+zreH4NlEQXxNRwvmefmi0kDQdAp47iBGgk7CY/wt2Kr2/L8ggmKuSeVzP0Fthcx1CrUSKX42Ae8TpJ0EXJgbIv2cxshwJ8NfuuaxDobqdCJ6k3P5slwLHxVbcw4lvp3R+dVl0p31SoqqN7dFRiH2EFWYF/ejojdpM7cMWv8ZQrieGD7AiYPprqj3ETAmVztHiDXV8riJgwNZi/54KbZPSp79h3CsPBJBsJA68z6p+J4t4aQ0CYN0T4lTDflEeGi5vGtJBun4+j1Tw1tQy5/KY80SZUMan1hC8Nhi0WdqBvymPf6qqpXdNyfrb7J/j5kLqr+NUARM36ILh8GAQNheTrKKMM6/W6or1gTAifr6LaSfWVovg6mgWj+K7xHXxI8QVi4Ye6OY1lVVq3f6z9Oa1S18fGfB122P8t8crAnfRfPFSlcr6Na6WEG4LSCOYIuF4JVwzQ93Qm3gVHc3Gv4/wBh5pwAljNVtxFOYUMThZWXi2CSmVhYmyoZoJlZlTEIGIpQnKSZYiknToGIZksyaEoTSSScMmwRrCdjcVUbmbSIH/kWtJ/2uMphi4Pw51evSot+ao9jB4uIH3X17guHMw9BlGmAGU2taABawifE6+a8N/SDsRWp8TZUrsytpNc9veBl3yj5T1Jv0Xu2MrQFFuANxjr+w2Frk+SDvxEgz6fX7fVa8fX2HK++4nx/uubx+Mh1jp7wfuUtV8V8VxRgxsZ167eayYDEd1rtCHu9A4kfQLPjcVI6C/8ARSwAPw+cvMeGn3Pqpoej4XFZ6YPQf3W7hJlx8FzvBah+FB2+yP8AAn3eDqQD9kufp3408QFjAlef8c4NVdVa+mHhzXZhlB1GkxrfbxXoeNqkaLOcbaDqn1xpc9YxPwj6lFjnNyvLRmabQ6L6nmgOI4XVP7Ynm4ewKLYvF5tXEAb7+nJBcbiM1mYhzYm+WSn4gI4tif4WHViGQDGZwM6HbwWVmLbUAIcDIBB2dO46KOO7PjEmK+Ke9o2DWtH9T6oRi69OhWFKiyq4aScoFrSDuFUmUWbBprgfH0WYEB8mZNh901OpqVCg+XelunMLZiPYR3dKwl0vI5ffVXNqd0/nmqaBkydSmG5z4puJP7T7FeH4iS89Tdev8cxnw8NWcbAMcOdyMo+pXk1KHJdfxt+OKiEs+3RXuaBqVVUpjUFTWoQ8XUCFOobqJICzSTQokJGqFE1EJ0oSUcyaUy08J1CUkYNdbwv9Oa9Q/wA2KQ5fM6eUCw8yi7f0uZE/GdH+lq7DC1Ic0F1psDqejb6q7E1QJGv0j86LXxjPyrl+FcHoYZ4a1kVdWufcu0FnaCb2C6CnJdLhA56xf2WfilH4rMpaHZSLXOYC8WFiVo4VQJF3EttHPeWu5kQlh33Ndn2MH853RkDmJIldDj6kX/PFc92QcPikRDi0nXqJhHeKHulY/l+q4czjqskyY0gdN/WfoucxLLu63+mv3XQYlhJPW3heJ9/oguM1d09hp7KOV0JxOngFc7FZGUxPyiT1JMgfWPJUYp3nusFaod7kXk/SEUczXonCMTLB1ifc3RzA4qKs87esR7LkuyOJmmZN5MDkO6AfQCyNVasDwv8An1Uw7HT4zEAgcjr9EFxOKNxzn/iSPLun/wCShWxWalmB116HdABj3E3kw4HUSf2n6OK18kYJ4ok90aTz2Jt+dEHxoZMXG8g381sfjWzN97b67eQ9kIxfEcxuI5zzVwqG8U4dScCXvfH/ALhH0C5viTadENGd9EHQwc7v9OYSZ8F1gxxuKdMvd/4sn1cYA9Vzx46HVXCq3v0yALBwBm/e0mORTz2JbjdVJFNjSSSdzr3RInnK24Rmn0/PzZYHVxUeIFgBHrPv7Ivgmq4zqeJrQ2Jv/VSwzrIbXrTUPKUQo6AIJyn6m8VLaDKTf/6Ok/6WafU/RebCs6dSuj7d8R+Li3DamMg8vm+srnWuhZde6359QzsQ7mUhiiEnGVAgKVW1Bz5USnKSpmZJOkmDJ4SSSI0JJ0kB71TrsFmgHnafDVJzmOkjc3iB5jqqacCBBvrv5ytDMJIsBOkLdmag8EQMx6mO9POy1YWi1kNB1JPO5VTqWQAAAE6nWAraNUb311GqYdD2TJOIJdYBhIEc7a9Ed4jUugPZd01Te+UwItCJcSxeWZn3XN+b614CMUAAfT+/uuZ4lXhx8/z6orxDizb38vL89VynEuIAyfFZRpfampiwfU/T/Cxvde1/yAhtXHCYnmVrFXfa0fRFaTnB7szijSqnMe6QfpeB5hdrWrS2eYErzD+NNzMRYR+dUd7O9pQ8ZX6fKPIqfhWX66jD48MIa75HwD0nf191XicGGGRcHQ/4WPHm58iPULncXxt7LNcYsI1A2VRGCmKxbg477IeMbULoAzTtv9FzPEO0NQy0naZC1/p/i82NbMkuDoGt4kz6K9weH9EuI9rD8oqsaBbLm3HhfyQurjTiHNDbhgMnmSbkDwUO0fYN7ajnYdwyEk5HA9ydmuGoHX6qXZ/gzqUl7szjFgIAAvbmT9lfHXkmzBvDUdPT+3siufIxzuQWOj00WXj3EQxrWbuueg/PZbRj9pYV/NGcK4ETO35K5DCViT3jaV11DBsqUXMNszYny11Sh9THieNdNR53LnH1JKzmUU4/wd+GrupvERcHZw2c07hC5HNY2e2v6SEpnBNbmkUjVFJIplSCSSSlAJJJJBGSTpID3amzyPVEaDSREGOfOFkoUw1xnXebkei0idS6AdJM/Rbs19SkJkmIGl56BR+CBvEH8ug/EOJQS1oJedIgmRzO2hWjhvDz81V7nknQFwYAdBlPzE31CWqx0fYzGU6lZxYcwaCCQDl8jEH6o1xWqHAoZg6op0HvaLwGtG9hJHso1eJZ8Mx7RqJIO0GHZvQrPpXLmOMcPDyRHpquZxfASZAcJuYmCu54xj208XTDrN/mf/WlUf8A/kLhOOdpg2o5zA1zKwa2ct8pBdYbGHA/7VjjWa5PH0CyqOs+0qzD8QdpBJ/Db6I3h+GDE1A4kgNZoWkG0SfNHMLwptICAJnWJuq8VXvHMYfMRdpE9D4+ivaHyMjXAAi+UwIuPzxXStwTnZXNbYz3u60NGkkF0kQFtpcKymc+YEWFsoA0Iix5XReNH+oaeLuLDmEOi3LQBc5xfGm8McbDQbi0rtBTa4lwYC3mGgzvaJEdQrcXw9uWW0wZESGR5a6onGJnbyCpXe5xJa4WjQ+a739H+GF1StXI7tNuUf6n6/QfVaKuDkSWtjoTMzEQdfHqu3wGFbQwzGMtLQ59o7zgC70sPJT3Mh+Wh+IpGXHnp7oZRwmYo5iagADiYG3Xqs2LY1ly4SfIieqf4vTPv2Gvw2S5sBr4ayvPOL8UfVqveAS39ovIAMA20/uvUMXRNSi6m43cO6Z8wD46Lh6PC4eRbIZg65SeZ2Gmq6LPSObgXS4qBSLDOYS4HkWCTPjp4ldV2e40w5ZcA5uQGbAtfOW/OQfVBqvC/wD1GixNxv8AnTQhC+I8GFIFznPLCWw0OEj/AMTYzrIO/il8VbL6dF2twArYOsCQauHe57b95rSZcD0c246tC8tyorxfiFX4tQPeSXAAxYOaLs02gg+aFSp6ulJh8qfImBTFyhRoSSSTSZJOkmDJJ0kAkkkkg96YwAERry9oHgmqFxEAlul9z0br6qumCTv6RC1UwOd+kStUGweEyxAM6k2i/jcogHy3bxgn21Wam0iZPrdWvcQNbWtt42QbH2k4zVpYQii0l0EB0gESRLgB0BHmuaxvbd7MBTpUmVfiW+IXU9jmc4Tpdx22K6x7Mxv63+4WWrwof4tG2o6FRedXOscA7F4rG13uDXMc+oagM/ISA2BblbwRng3Zf4Yc6q74joIaCSAI8OkbLozwyLtJbtLYkjzB/AtGDYbseC61nSGuI5EQNLePkiTDvWhHwvh5TbJoTlJItG5vccpW6hgM0Ejum8CQDy63t0WrEYLMYDo6Af8AITHLZaKXdAzTeLRmPSYFtrkp4hnw9JzRDjpJyzlJnSTsJn3VooBokwM0mNLTaBt+FLFVssyHDcQIOulhz8Vho1TZrjJJmM9xM5rb/wCUYYg1oEhgA0mAOZ/p7LNVxmSTYRq7MwfRp940V7KJIiLEwQB3fPp/daaNMyQ45QbRl7p0tmaDaUEDYHiDanxHOY8GjTzhrg0MquFmBrupjnYob2n4niqWIo0j+9lIPbsajnD4lxsII8F1NXhjW7Ngtg6mb6EboZxDgVN9QVqgzVAQA4l2axkAQeai8WrnUjj8V2hxAYxrnj4gJJcQCBBJaIiNo0srOO8UqGiCHyW5S9wOh3I5gFGanZGi50lpeCZhznOEkybE81dU7LUcvdY0chl2tY9LK5zYV65Q4Vx2m5pcXgthsOkd4gXMIDiBUuWAESYzNgtBM6k32RqnwJoIimzxDYMaWgKf/TI0a02Phe33+i0ZgOLxDnNLXAROoBaZ52KxUsSPgubWBtmbmEC7ASCOYjT72XSDDFpBc0Ebk2O2n9UL41w4HvtZmFpaLZgARIka3IPMAboz+HK5HtLTY9lOqwiYDHgEWgHIbaAgHyAXPrp6VLNha1Et77DmAjvWv5xBH+4c1zCxq0gExCQSSBkkkkESSSSASSlTplxAAJJsALk+ARzAdja1QS4tYJAgyXbftHjzTk0AKS7VvYekNX1Cd4ygf8T7lJPxpa76liJ0tzj77q+lUvFuc20mLXVLGjqq6mGpvc0mCdiCMwjcCZF9wqIUouMSft7FOXSdLAeY5KhtANFgfOf66qdMujQDkJzfWIBTNfTedSOn5y8FJlN0HLHmCbKmm0yJn7rWAeo8vrCCJrTYS0R+eaeoIcCHa6+WvL1KjnExc/7h7fZScyTcQPz8lLDVMxPfg3BNo001NusK2gxxPemLgTB623j+gVow4jeDt03UauEZBzAQdZ/oUYbPUsMrADt3Y25kGRGm6BHiNSi7L8N5Ie4mzT3CcwgTmADTGmoPVHqtVrWhrTDRYNY0AR0vIWVlWkCLEwPmMZhaLxeYQS6k1rmgh5yu0LXQTecp0A+y1CALCZtGp6yYQjEcXp0SMjGkCTJgFs6gE7zyjVX0eM/EY0nub962os7WNwnKMFGVCRBaWiNyD0gAHl4KNXDtIlxOmhJieYH5EK3CDu3dN5+aZ035dFGsG7uGpMxMJkzta1txN7y726JVaZmYJt9ArTWY0jMToBpA6Rvuk6oJIiZ8vT+/JMlFJhI+QgH83jVM+mdZ9vdWUKxDe6WgSRFgI81mdcyTI638bJknjsTSpNPxSA05W6EiXGLwJHiuY4xUZJyHM0EiQTMcwQug41hwGEDvMe3lsdRfTwXE8MpZXupPOcgZmk/ubBaHD2I2I6pHGHGPNOuKrcpa75xzIkBzTqHZZtvl5wuV7R4BtOrNO7H94cgf3AdL/WNkbqP+HiH0HAFjgSy/M5g0eDpA3BQ7j9TNSZDswaTIiCwm1+cxrvZZ1YAknhMVAJJW4XCOqOytEn0A6knRdDQ7H92X1BO4bYD/AHO/onJaHN06RcYAJPICT9F0PDOyLrPry1piGA99/pOXzujGFwDKbIp9wmcxiTHLNMnw/DdTpvLTfKN3aOj/ALcxPdHgtJx/Sa6eAo0I+E1rSBBHzOB5udt4FKriyAIuTqBb6qo04blb3Y0315eapfQbYzfrGtxrvPRUTWMaeTR4n+qSzfwZN41/OaSDdbTPfA2v7LfQF0klJNKsoDujwSSQZybKiq8wbn9ySSYa8GLeJM9dVNmp8vukklAz8TeRABIvshwcb/6kySVDFiNZ3mJ39Vlc85SZMyPskkg1OIYDiqQIBHdMG4nnC342+aeQP1N0klKv4XxnBpAJAtYEqdOofi6n9u/VOkqiavxzru8R91Zw55nU/N9kyS0/TP8AYlXbL3eH2WWfk8R90kkQVpcZpX2qNjprouH400DE0YEfzqg8jTaSPCbwmSSvw59Du1zB/DU3QMwcIO4k3goHxRvdf/qd/wASfe6ZJR205+OeKikksw6ns8P5bOpM9bxfmiODNj4n2TJLfn4lsoix/OSr4sYo2t/kJJJ34EGMGVthoT/dOT3XHeEkkgKYZoyNtsEkklC3/9k=" alt="embedded folder icon"></center><center>
    %s
    </center></body></html>"""



# Exceptions are for the weak. BLAME(matt)
def OhGodNow(error):
  print k_stupid_human
  print error
  sys.exit(1)

def IsSaveGame(filename):
  return k_savegame_re.match(filename)

# Oh, yeah. A player named, like, "CivBeyondSword" completely fucks this
# half-assed implementation.
def DiscoverMC(filename):
  for mc in k_sucka_mcs:
    if re.match(".*%s.*" % mc, filename):
      return mc

# Compares filenames by mtime.
def CompareSavegames(a, b):
  a_mtime = os.stat(os.path.join(k_civamints_dir,a)).st_mtime
  b_mtime = os.stat(os.path.join(k_civamints_dir,b)).st_mtime
  return int(round(a_mtime - b_mtime))

def GetSortedSavegames():
  savegames = filter(IsSaveGame, os.listdir(k_civamints_dir))
  # We're completely dependent below on the savegames sorting in reverse
  # chronilogical order.
  return sorted(savegames, CompareSavegames)

# savegames MUST be sorted in reverse chronological order.
# returns a list of (mtime, player) tuples.
def GetSaveTimes(savegames):
  save_times = []
  for game in savegames:
    stat = os.stat(os.path.join(k_civamints_dir,game))
    save_times.append((stat.st_mtime, DiscoverMC(game)))
  return save_times

# Returns (shame_by_mc, (best, mc), (worst, mc))
def GetShameByMC(save_times):
  global insertHtml
  shame_by_mc = {}
  worst = 0
  best = 100000000000000000
  for i in range(0, len(save_times) - 1):
    newer_time = save_times[i+1][0]
    older_time = save_times[i][0]
    # MC in PRIOR game gets credit. as in: MJW gets credit for time until JWM
    # savegame.
    mc = save_times[i][1]
    next_mc = save_times[i+1][1]
    shame = newer_time - older_time
    if shame < 0:
      #print "OH GOD! invalid shame: %s %d" % (mc, shame)
      continue
    if not (mc, next_mc) in k_valid_mc_pairs:
      #print "OH GOD! Missing save game? %s -> %s" % (mc, next_mc)
      continue
    if not mc in shame_by_mc:
      shame_by_mc[mc] = []
    shame_by_mc[mc].append(shame/60)
    if shame >= worst:
      worst = shame
      worst_mc = mc
    if shame <= best:
      best = shame
      best_mc = mc
  insertHtml=insertHtml+"<dd>Most Shameful Time: %d minutes (WAY TO GO, %s)<br>" % (worst/60, worst_mc)
  insertHtml=insertHtml+"Least Shameful Time: %d SECONDS (WAY TO GO, %s)<p>" % (best, best_mc)
  return shame_by_mc

# returns dictionary keyed by average shame in seconds, with values of the
# shamed MC. this makes it easy for a lazy person like me to rank the results by
# sorting the keys.
def GetAverageShame(shame_by_mc):
  avg_shame = {}
  for mc in shame_by_mc.keys():
    avg = sum(shame_by_mc[mc]) / len(shame_by_mc[mc])
    avg_shame[avg] = mc
  return avg_shame

# Standard disclaimers apply: savegames need to be sorted chronologically.
def ShameMCs(savegames):
  global insertHtml
  shame_by_mc = GetShameByMC(GetSaveTimes(savegames))
  avg_shame = GetAverageShame(shame_by_mc)
  insertHtml=insertHtml+"<ul>"
  for k in sorted(avg_shame.keys(), reverse = True):
    aLine= "<li>%s : %f minutes" % (avg_shame[k], k)
    #print aLine
    insertHtml=insertHtml+aLine
  insertHtml=insertHtml+"</ul></dd>"


if __name__ == "__main__":
  #try:
    if not os.path.exists(k_civamints_dir):
      OhGodNow("%s doesn't exist." % (k_civamints_dir))
    insertHtml=insertHtml+ "<h1>BEHOLD YOUR SHAME!</h1><p><table border=1><tr><td>"
    savegames = GetSortedSavegames()
    insertHtml=insertHtml+ "\n<h2>Last Round:</h2><p>"
    ShameMCs(savegames[0:(len(k_sucka_mcs)*2)])
    insertHtml=insertHtml+ "\n<h2>Last Ten Rounds:</h2><p>"
    ShameMCs(savegames[0:(len(k_sucka_mcs)*10)])
    insertHtml=insertHtml+ "\n<h2>All Time:</h2><p>"
    ShameMCs(savegames)
    insertHtml=insertHtml+ "\n</td></tr></table>"
    shamefulHtml=shamefulHtml%(insertHtml)
    theFile=open('shamefulMints.html', 'w')
    theFile.write(shamefulHtml)
    theFile.close()
    #probably should have a check to see if the file actually exists
    import webbrowser
    theCWD=os.getcwd()
    theFile="file:///%s/shamefulMints.html" % (theCWD)
    webbrowser.open(theFile)
    #print shamefulHtml
  #except Exception:
  #  OhGodNow("OMFG EXCEPTION: %s" % Exception)
