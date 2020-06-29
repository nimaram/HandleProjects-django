from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    
    def create_user(self,email,talents,password):
        
        if not email:
            raise ValueError('شما باید ایمیل خود را وارد کنید')
        if not talents:
            raise ValueError('شما باید مهارت های خود را وارد کنید')

        user = self.model(email=self.normalize_email(email),talents=talents)
        user.set_password(password)
        user.save(using=self._db)
        return user    
    def create_superuser(self,email,talents,password):
        user = self.create_user(email,talents,password)
        user.is_admin = True
        user.save(using=self._db)
        return user 