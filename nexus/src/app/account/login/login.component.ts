import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { UserService } from 'src/app/services/users/user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent {
  LoginForm: FormGroup;
  constructor(private fb: FormBuilder, private user: UserService) {
    this.LoginForm = this.fb.group({
      email: ['', Validators.required],
      password: ['', Validators.required],
    });
  }

  onSubmit() {
    if (this.LoginForm.valid) {
      const formData = this.LoginForm.value;

      this.user.login(formData);
    }
  }
}
