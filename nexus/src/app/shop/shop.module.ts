import { NgModule, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductComponent } from './product/product.component';
import { ShopComponent } from './shop.component';
import { ShopdetailsComponent } from '../shopdetails/shopdetails.component';
import { MatCardModule } from '@angular/material/card';
import { MatTableModule } from '@angular/material/table';
import { ShopCreateComponent } from './shop-create/shop-create.component';
import { MatDialogModule } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ProductCreateComponent } from './product-create/product-create.component';

@NgModule({
  declarations: [
    ProductComponent,
    ShopComponent,
    ShopdetailsComponent,
    ShopCreateComponent,
    ProductCreateComponent,
  ],
  imports: [
    FormsModule,
    ReactiveFormsModule,
    CommonModule,
    MatCardModule,
    MatTableModule,
    MatDialogModule,
    MatButtonModule,
  ],
})
export class ShopModule {}
