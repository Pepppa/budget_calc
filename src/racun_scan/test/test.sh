#!/bin/bash

dir=$(dirname $0)
mainpy=${dir}/../py/main.py

test1 () {
    python3 $mainpy --htmlfile ${dir}/20240730_full_racun.html
}

test2 () {
    python3 $mainpy --link https://suf.purs.gov.rs/v/?vl=A0FERlA5OVJRQURGUDk5UlHvgQQALYEEAFA0SAEAAAAAAAABkQ9sdeAAAACb24Vkglu+RxghtJVpiwb2DtENyMngq+jUGyQRj1xCaNhObccrAJWDreC6VlpwxIU0HiYI1onZg2Jl+GaGrBYWFagR1w3w+aTraguIJ9u4lGh8IbjefQ7MjwPL2+wzFu6GQUMPSLjGkL3XQl3dlZ5QkrG6u7HsYv1no9YwSXNwC9+XwWx7P+2Q8pJxCuWAxVn2/XdmfzvOsWS6NfqcR0to5vQb6Nj2zw3pxvdpGYg5qqHO60zRmhZCMl/nJC6WAJI1tiySr/fgzIjTZOSxpo3ZRw80JayFcg8cvQuxeOO8utQTJln+5C6Bt26LVysMYjyHr+NLxdD+0H2ANkHK9otZUJDE1GXEUIKfEtpkRN0tZY3IrmGqsinop+Gq4dBO/DshMPPNf8r59c2ODStkFleY0e9m8pJyBoBPj/fhSE7VwaheGqyIcNN6Ucaex6JE5WIKsY4YOhvu2kAr7M3y6DvckUHirrDsuafrWGon01aFZ+uZA2zTUXkHE37GoQgur5YTjpvKDnW9DZwqRxJik8dAOBcsJ8L1rg5uABn4wzp/N8nTv2y6JWa9f7celKLvaOGgE74IQ7eaqEC1FFwHd1Qii2KRHbYQom2jkiBzaKoxPNypdtZG+R8UilEo0Vdid4vTVoGN5mLv+HBO2HCcFTIe0711r/KYZMaVdaafvFs3Yuv/kbUKtUPEdNdx5h2gp7M=

}

test3 () {
    python3 $mainpy --csvfile ${dir}/mani_app_racuni.csv
}

test3
