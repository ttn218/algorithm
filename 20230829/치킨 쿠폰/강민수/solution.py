def order(chichen, coupon):
    newCoupon = chichen + coupon
    
    serviceChichen = int(newCoupon / 10)
    restCoupon = newCoupon % 10
    
    if serviceChichen + restCoupon >= 10:
        return serviceChichen + order(serviceChichen, restCoupon)
    
    return serviceChichen


def solution(chicken):
    answer = order(chicken, 0)
    
    return answer