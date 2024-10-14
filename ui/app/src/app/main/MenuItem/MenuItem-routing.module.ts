import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MenuItemHomeComponent } from './home/MenuItem-home.component';
import { MenuItemNewComponent } from './new/MenuItem-new.component';
import { MenuItemDetailComponent } from './detail/MenuItem-detail.component';

const routes: Routes = [
  {path: '', component: MenuItemHomeComponent},
  { path: 'new', component: MenuItemNewComponent },
  { path: ':id', component: MenuItemDetailComponent,
    data: {
      oPermission: {
        permissionId: 'MenuItem-detail-permissions'
      }
    }
  },{
    path: ':menu_item_id/MenuItemPromotion', loadChildren: () => import('../MenuItemPromotion/MenuItemPromotion.module').then(m => m.MenuItemPromotionModule),
    data: {
        oPermission: {
            permissionId: 'MenuItemPromotion-detail-permissions'
        }
    }
},{
    path: ':menu_item_id/MenuItemSupplier', loadChildren: () => import('../MenuItemSupplier/MenuItemSupplier.module').then(m => m.MenuItemSupplierModule),
    data: {
        oPermission: {
            permissionId: 'MenuItemSupplier-detail-permissions'
        }
    }
},{
    path: ':menu_item_id/OrderItem', loadChildren: () => import('../OrderItem/OrderItem.module').then(m => m.OrderItemModule),
    data: {
        oPermission: {
            permissionId: 'OrderItem-detail-permissions'
        }
    }
},{
    path: ':menu_item_id/Review', loadChildren: () => import('../Review/Review.module').then(m => m.ReviewModule),
    data: {
        oPermission: {
            permissionId: 'Review-detail-permissions'
        }
    }
}
];

export const MENUITEM_MODULE_DECLARATIONS = [
    MenuItemHomeComponent,
    MenuItemNewComponent,
    MenuItemDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MenuItemRoutingModule { }