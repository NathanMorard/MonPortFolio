import win32com.client as win32
import pythoncom

class mail:
    @staticmethod
    def send_email(message, dest, obj):
        pythoncom.CoInitialize()
        
        try:
            outlook = win32.Dispatch('outlook.application')
            
            mail = outlook.CreateItem(0)
            mail.Subject = obj
            mail.Body = message
            mail.To = dest

            for account in outlook.Session.Accounts:
                if account.DisplayName == 'nathannotifier@outlook.com':
                    mail._oleobj_.Invoke(*(64209, 0, 8, 0, account))

            mail.Send()
            return True, "Email envoyé avec succès !"
            
        except Exception as e:
            return False, f"Erreur lors de l'envoi de l'email : {str(e)}"
            
        finally:
            pythoncom.CoUninitialize()