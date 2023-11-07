import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ShopService } from 'src/app/services/shops/shop.service';

@Component({
  selector: 'app-product-create',
  templateUrl: './product-create.component.html',
  styleUrls: ['./product-create.component.scss'],
})
export class ProductCreateComponent implements OnInit {
  productForm!: FormGroup;
  shop_id!: string;

  constructor(private formBuilder: FormBuilder, private shop: ShopService) {}

  ngOnInit() {
    this.productForm = this.formBuilder.group({
      name: ['', [Validators.required]],
      price: [0, [Validators.required]],
      description: ['', [Validators.required]],
      stock: [0, [Validators.required]],
      measurement: ['', [Validators.required]],
      shop: ['', [Validators.required]],
      category: ['', [Validators.required]],
    });
  }

  onSubmit() {
    if (this.productForm.valid) {
      this.productForm.value.shop = this.shop_id;
      try {
        this.shop
          .createProducts(this.productForm.value)
          .subscribe((response) => {
            console.log(response);
          });
      } catch (error) {
        console.log(error);
      }
    }
  }
}
