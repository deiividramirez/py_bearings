#!/usr/bin/env python3

from pathlib import Path
WORKSPACE = Path(__file__).parent.absolute().parent.absolute()

import cv2
from cv_bridge import CvBridge


def saveFront(msg, args = ("N/",)):
    print(f"[INFO] Calling saveFront for drone {args[0]}")
    actual = (CvBridge().imgmsg_to_cv2(msg))
    cv2.imwrite(f"{WORKSPACE}/data/desired_{args[0]}f.jpg", actual)
    print(f"[INFO] Desired image saved for drone {args[0]} at {WORKSPACE}/data/desired_{args[0]}f.jpg")


def saveUnder(msg, args = ("N/",)):
    print(f"[INFO] Calling saveUnder for drone {args[0]}")
    actual = (CvBridge().imgmsg_to_cv2(msg))
    cv2.imwrite(f"{WORKSPACE}/data/desired_{args[0]}u.jpg", actual)
    print(f"[INFO] Desired image saved for drone {args[0]} at {WORKSPACE}/data/desired_{args[0]}u.jpg")