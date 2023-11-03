import { CanActivateFn } from '@angular/router';

export const shopsGuard: CanActivateFn = (route, state) => {
  return true;
};
