import { CanActivateFn, Router } from '@angular/router';
import { UserService } from './services/users/user.service';
import { inject } from '@angular/core';

export const shopsGuard: CanActivateFn = (route, state) => {
  const user = inject(UserService);
  const router = inject(Router);
  if (!user.isLoggedIn()) {
    router.navigate(['/']);

    return false;
  } else {
    return true;
  }
};
