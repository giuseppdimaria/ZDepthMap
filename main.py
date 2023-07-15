import generate_ZDepthMap as ZDepthGen
import points_cloud_generator as PointsCLoudGen
import mesh_generator as MeshGen



def main():
    image, output = ZDepthGen.ZDepth_generator()
    pcd = PointsCLoudGen.points_cloud_generator(image, output)
    MeshGen.mesh_generator(pcd)


if __name__ == "__main__":
    main()