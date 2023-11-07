import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ShopService } from 'src/app/services/shops/shop.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-shop-create',
  templateUrl: './shop-create.component.html',
  styleUrls: ['./shop-create.component.scss'],
})
export class ShopCreateComponent implements OnInit {
  shopForm!: FormGroup;
  constructor(
    private http: HttpClient,
    private shop: ShopService,
    private fb: FormBuilder
  ) {}

  ngOnInit() {
    this.shopForm = this.fb.group({
      name: ['', Validators.required],
      address: ['', Validators.required],
      phone: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      description: ['', Validators.required],
    });
  }
  onSubmit() {
    if (this.shopForm.valid) {
      try {
        this.shop.createShop(this.shopForm.value).subscribe((response) => {
          console.log(response);
        });
      } catch (error) {
        console.log(error);
      }
    }
  }
}
