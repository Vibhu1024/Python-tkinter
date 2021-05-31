#an easy to use Pyton library for displaying windows 10 notifications which is useful for Windows GUI development.
import win10toast
toaster=win10toast.ToastNotifier()
toaster.show_toast('Python','HEY! VIBHU python is working properly',duration=5)