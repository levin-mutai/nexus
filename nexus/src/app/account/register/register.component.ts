import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { UserService } from 'src/app/services/users/user.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss'],
})
export class RegisterComponent implements OnInit {
  ngOnInit(): void {}
  RegisterForm: FormGroup;
  constructor(private fb: FormBuilder, private user: UserService) {
    this.RegisterForm = this.fb.group({
      username: ['', Validators.required],
      email: ['', Validators.required],
      full_name: ['', Validators.required],
      password: ['', Validators.required],
    });
  }

  onSubmit() {
    if (this.RegisterForm.valid) {
      const formData = this.RegisterForm.value;

      this.user.register(formData);
    }
  }
}
