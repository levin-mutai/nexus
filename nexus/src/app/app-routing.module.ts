import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AccountComponent } from './account/account.component';
import { ShopComponent } from './shop/shop.component';
import { LoginComponent } from './account/login/login.component';
import { RegisterComponent } from './account/register/register.component';
import { ShopdetailsComponent } from './shopdetails/shopdetails.component';
import { shopsGuard } from './shops.guard';

const routes: Routes = [
  { path: '', component: LoginComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'accounts', component: AccountComponent },
  {
    path: 'shops/:id',
    canActivate: [shopsGuard],
    component: ShopdetailsComponent,
  },
  { path: 'shops', canActivate: [shopsGuard], component: ShopComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
