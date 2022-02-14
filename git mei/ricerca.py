import webbrowser as link
print('vuoi fare una ricerca o vuoi un immagine?')
cosa_vuoi= input()
if (cosa_vuoi == 'immagine'):
    print('ottimo, che ' + (cosa_vuoi)+ ' vuoi?')
    immagine = input('digita qui la tua immagine ')
    URL = ('https://www.google.it/search?q=' + (immagine) + '&tbm=isch&ved=2ahUKEwjHxb6ns-_zAhUHw-AKHb-ADlMQ2-cCegQIABAA&oq=' + (immagine) + '&gs_lcp=CgNpbWcQAzIHCCMQ7wMQJzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzoHCAAQsQMQQzoECAAQQzoFCAAQgAQ6CAgAELEDEIMBUIoHWIcOYL0PaABwAHgAgAGgAYgBuQaSAQMwLjaYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=b8t7YYfSJIeGgwe_gbqYBQ&bih=657&biw=1366')
    link.open(URL)
else:
    if (cosa_vuoi == 'ricerca'):
         print('ottimo, vuoi fare una ' + (cosa_vuoi))
         ricerca = input('digita qui quello che vuoi ricercare ')
         URL =('https://www.google.it/search?q=' + (ricerca) + '&sxsrf=AOaemvIZ9UBUWKKDD6EqAd21-KDl5QXSAQ%3A1635502763481&source=hp&ei=q8p7Ybn7GZuPxc8P18Gj-Ao&iflsig=ALs-wAMAAAAAYXvYu5X9Qju5PDgRHMe6wcS6koVxk8MH&oq=' + (ricerca) + '&gs_lcp=Cgdnd3Mtd2l6EAMyBwguEEMQkwIyBwguELEDEEMyBwgAELEDEEMyBwguELEDEEMyBwguELEDEEMyCAguEIAEELEDMgcILhCxAxBDMgQILhBDMgQILhBDMgQIABBDOgcIIxDqAhAnOgQIIxAnOgsIABCABBCxAxCDAToRCC4QgAQQsQMQgwEQxwEQ0QM6CAgAEIAEELEDOggIABCxAxCDAToQCAAQgAQQhwIQsQMQgwEQFDoKCAAQsQMQgwEQQzoNCC4QsQMQgwEQQxCTAlCkFFjdIWCuI2gBcAB4AIABtQGIAacFkgEDMC40mAEAoAEBsAEK&sclient=gws-wiz&ved=0ahUKEwj5_PjJsu_zAhWbR_EDHdfgCK8Q4dUDCAk&uact=5')
         link.open(URL)