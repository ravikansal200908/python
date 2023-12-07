from threading import current_thread

obj = current_thread()

print("Daemon nature of main thread : ", obj.daemon)
