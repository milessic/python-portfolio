import inspect
class PythonSryton:
    def run(self, locals=locals):
        import sys
        import readline
        history = []
        history_counter = -2
        history_show = False
        inp = ""
        import platform
        
        # argv
        tryb_odporny = True if "--tryb-odporny-psychicznie" in sys.argv else False
        
        print(f"PythonSryton - upośledzona wirtualna muszelka Pythona v.1 pracująca na Python {platform.python_version()}")
        print("żeby udusić PythonSryton, użyj do_widzenia(), spadaj() albo Ctrl+D")
        
        def spadaj():
            if tryb_odporny:
                print("Trochę kultury, poza tym sprawdź lokalne centra terapii w okolicy.")
                return
            print("NARA")
            raise EOFError
        
        def do_widzenia():
            print("Do zobaczenia następnym razem!")
            raise EOFError
        dzięki = "luzik"
        while True:
            try:
                try:
                    raise SyntaxError
                    inp = input(">>> ")
                    if inp != r"^[[A":
                        eval(inp)
                except (SyntaxError):
                    inp = input(">>> ")
                    exec(str(inp))
            except NameError as e:
                print(f"NameError mordko: {e}")
            except EOFError:
                break
            except SyntaxError as e:
                print(f"SyntaxError: {e}")
            except AttributeError as e:
                print(f"No nie AttributeError!: {e}")
            except Exception as e:
                print(f"{type(e).__name__} pierdyknął: {e}")
            finally:
                history.append(inp)
            if inp == "dzięki":
                dzięki()
            inp = ""

if __name__ == "__main__":
    PythonSryton().run()

