import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SupplierHomeComponent } from './home/Supplier-home.component';
import { SupplierNewComponent } from './new/Supplier-new.component';
import { SupplierDetailComponent } from './detail/Supplier-detail.component';

const routes: Routes = [
  {path: '', component: SupplierHomeComponent},
  { path: 'new', component: SupplierNewComponent },
  { path: ':id', component: SupplierDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Supplier-detail-permissions'
      }
    }
  },{
    path: ':supplier_id/MenuItemSupplier', loadChildren: () => import('../MenuItemSupplier/MenuItemSupplier.module').then(m => m.MenuItemSupplierModule),
    data: {
        oPermission: {
            permissionId: 'MenuItemSupplier-detail-permissions'
        }
    }
}
];

export const SUPPLIER_MODULE_DECLARATIONS = [
    SupplierHomeComponent,
    SupplierNewComponent,
    SupplierDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SupplierRoutingModule { }