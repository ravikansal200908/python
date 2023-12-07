import threading
import time

number_of_player = 4
barrier = threading.Barrier(number_of_player)


def player(name) -> None:
    print(f"{name} started")
    score = 0
    for i in range(5):
        time.sleep(3)
        print(f"{name} is playing")

    barrier.wait()
    # barrier

    # code for session killing
    # code for desplaying final result
    print(f"{name} score {score}")
    # code for sending winning amount into accounts
    print(f"sending winning amount to {name}")


player_names = ["amit", "sumit", "mohit", "sahil"]

thread_list = []
for name in player_names:
    thread = threading.Thread(target=player, args=(name,))
    thread_list.append(thread)
    thread.start()
