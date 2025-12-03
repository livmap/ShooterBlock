def collision(cX, cY, r, rX, rY, rW, rH):
    collide = False
    if abs(cX - rX) <= r + (rW / 2) and abs(cY - rY) <= r + (rH / 2):
        collide = True
    return collide

