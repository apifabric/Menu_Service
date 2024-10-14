import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RestaurantHomeComponent } from './home/Restaurant-home.component';
import { RestaurantNewComponent } from './new/Restaurant-new.component';
import { RestaurantDetailComponent } from './detail/Restaurant-detail.component';

const routes: Routes = [
  {path: '', component: RestaurantHomeComponent},
  { path: 'new', component: RestaurantNewComponent },
  { path: ':id', component: RestaurantDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Restaurant-detail-permissions'
      }
    }
  },{
    path: ':restaurant_id/Employee', loadChildren: () => import('../Employee/Employee.module').then(m => m.EmployeeModule),
    data: {
        oPermission: {
            permissionId: 'Employee-detail-permissions'
        }
    }
},{
    path: ':restaurant_id/MenuItem', loadChildren: () => import('../MenuItem/MenuItem.module').then(m => m.MenuItemModule),
    data: {
        oPermission: {
            permissionId: 'MenuItem-detail-permissions'
        }
    }
},{
    path: ':restaurant_id/Order', loadChildren: () => import('../Order/Order.module').then(m => m.OrderModule),
    data: {
        oPermission: {
            permissionId: 'Order-detail-permissions'
        }
    }
}
];

export const RESTAURANT_MODULE_DECLARATIONS = [
    RestaurantHomeComponent,
    RestaurantNewComponent,
    RestaurantDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class RestaurantRoutingModule { }