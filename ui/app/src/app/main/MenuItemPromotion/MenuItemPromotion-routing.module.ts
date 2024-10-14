import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MenuItemPromotionHomeComponent } from './home/MenuItemPromotion-home.component';
import { MenuItemPromotionNewComponent } from './new/MenuItemPromotion-new.component';
import { MenuItemPromotionDetailComponent } from './detail/MenuItemPromotion-detail.component';

const routes: Routes = [
  {path: '', component: MenuItemPromotionHomeComponent},
  { path: 'new', component: MenuItemPromotionNewComponent },
  { path: ':id', component: MenuItemPromotionDetailComponent,
    data: {
      oPermission: {
        permissionId: 'MenuItemPromotion-detail-permissions'
      }
    }
  }
];

export const MENUITEMPROMOTION_MODULE_DECLARATIONS = [
    MenuItemPromotionHomeComponent,
    MenuItemPromotionNewComponent,
    MenuItemPromotionDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MenuItemPromotionRoutingModule { }