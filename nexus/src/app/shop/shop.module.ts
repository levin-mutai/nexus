import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProductComponent } from './product/product.component';
import { ShopComponent } from './shop.component';
import { UserService } from '../services/users/user.service';

@NgModule({
  declarations: [ProductComponent, ShopComponent],
  imports: [CommonModule],
})
export class ShopModule {}
